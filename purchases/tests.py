from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from materials.models import Material, Unit
from purchases.models import PurchasesOrder, LinesPurchasesOrder
from suppliers.models import Country, Currency, Supplier
from users.models import Role

User = get_user_model()


class PurchaseOrderFormSetTestCase(TestCase):
    def setUp(self):
        self.role = Role.objects.create(
            name='Admin Role',
            purchases=3,
            materials=3,
            suppliers=3,
            customers=3,
            sales=3,
            inventory=3,
            accounting=3,
            reporting=3
        )
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
            role=self.role,
            is_staff=True
        )
        self.country = Country.objects.create(name='Chile')
        self.currency = Currency.objects.create(name='CLP')
        self.supplier = Supplier.objects.create(
            name='Proveedor Test',
            legal_name='Proveedor Test SpA',
            tax_id='76123456-7',
            country=self.country,
            state_province='RM',
            city='Santiago',
            address='Av. Siempre Viva 123',
            zip_code=12345,
            phone=912345678,
            email='test@proveedor.com',
            contact_name='Juan Perez',
            contact_role='Ventas',
            category='General',
            payment_terms='30 dias',
            currency=self.currency,
            payment_method='Transferencia',
            bank_account='123456789'
        )
        self.unit = Unit.objects.create(name='Unidad', symbol='UND')
        self.material1 = Material.objects.create(name='Tornillo', description='Tornillo 2 pulg', unit=self.unit)
        self.material2 = Material.objects.create(name='Tuerca', description='Tuerca 2 pulg', unit=self.unit)

        self.client = Client()
        self.client.login(username='testuser', password='testpassword123')

    def test_create_purchase_order_with_multiple_lines_via_view(self):
        url = reverse('purchases:purchase_create')
        data = {
            'action': 'add',
            'supplier': self.supplier.id,
            'estimated_delivery_date': date.today().strftime('%Y-%m-%d'),
            # FormSet Management Form fields
            'lines_purchases_order-TOTAL_FORMS': '2',
            'lines_purchases_order-INITIAL_FORMS': '0',
            'lines_purchases_order-MIN_NUM_FORMS': '0',
            'lines_purchases_order-MAX_NUM_FORMS': '1000',
            # Line 0
            'lines_purchases_order-0-material': self.material1.id,
            'lines_purchases_order-0-quantity': 10,
            'lines_purchases_order-0-unit_material': self.unit.id,
            'lines_purchases_order-0-price': 500,
            'lines_purchases_order-0-currency': self.currency.id,
            # Line 1
            'lines_purchases_order-1-material': self.material2.id,
            'lines_purchases_order-1-quantity': 25,
            'lines_purchases_order-1-unit_material': self.unit.id,
            'lines_purchases_order-1-price': 1200,
            'lines_purchases_order-1-currency': self.currency.id,
        }

        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)

        # Check that exactly one purchase order was created
        self.assertEqual(PurchasesOrder.objects.count(), 1)
        po = PurchasesOrder.objects.first()
        self.assertEqual(po.supplier, self.supplier)
        self.assertEqual(po.created_by, self.user)

        # Check that 2 lines were created and linked automatically to po
        lines = LinesPurchasesOrder.objects.filter(purchase_order=po).order_by('position')
        self.assertEqual(lines.count(), 2)
        self.assertEqual(lines[0].material, self.material1)
        self.assertEqual(lines[0].quantity, 10)
        self.assertEqual(lines[0].price, 500)
        self.assertEqual(lines[0].created_by, self.user)

        self.assertEqual(lines[1].material, self.material2)
        self.assertEqual(lines[1].quantity, 25)
        self.assertEqual(lines[1].price, 1200)

    def test_get_create_purchase_order_view(self):
        url = reverse('purchases:purchase_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertIn('formset', response.context)
        self.assertContains(response, 'lines_purchases_order-TOTAL_FORMS')
        self.assertContains(response, 'empty-form')
        self.assertContains(response, 'Agregar línea')

    def test_create_purchase_order_invalid_formset_does_not_save_order(self):
        url = reverse('purchases:purchase_create')
        data = {
            'action': 'add',
            'supplier': self.supplier.id,
            'estimated_delivery_date': date.today().strftime('%Y-%m-%d'),
            # FormSet Management Form fields
            'lines_purchases_order-TOTAL_FORMS': '1',
            'lines_purchases_order-INITIAL_FORMS': '0',
            'lines_purchases_order-MIN_NUM_FORMS': '0',
            'lines_purchases_order-MAX_NUM_FORMS': '1000',
            # Line 0 with invalid/incomplete data (changed but missing required fields)
            'lines_purchases_order-0-quantity': 10,
            'lines_purchases_order-0-material': '',
            'lines_purchases_order-0-unit_material': '',
            'lines_purchases_order-0-price': '',
            'lines_purchases_order-0-currency': '',
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

        # Ensure nothing was saved due to invalid formset
        self.assertEqual(PurchasesOrder.objects.count(), 0)
        self.assertEqual(LinesPurchasesOrder.objects.count(), 0)

    def test_get_update_purchase_order_view(self):
        po = PurchasesOrder.objects.create(
            supplier=self.supplier,
            estimated_delivery_date=date.today(),
            created_by=self.user
        )
        line = LinesPurchasesOrder.objects.create(
            purchase_order=po,
            material=self.material1,
            quantity=5,
            unit_material=self.unit,
            price=100,
            currency=self.currency,
            created_by=self.user
        )
        url = reverse('purchases:purchase_update', kwargs={'pk': po.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertIn('formset', response.context)
        self.assertEqual(response.context['action'], 'edit')

    def test_update_purchase_order_and_lines_via_view(self):
        po = PurchasesOrder.objects.create(
            supplier=self.supplier,
            estimated_delivery_date=date.today(),
            created_by=self.user
        )
        line1 = LinesPurchasesOrder.objects.create(
            purchase_order=po,
            material=self.material1,
            quantity=5,
            unit_material=self.unit,
            price=100,
            currency=self.currency,
            created_by=self.user
        )
        url = reverse('purchases:purchase_update', kwargs={'pk': po.pk})
        data = {
            'action': 'edit',
            'supplier': self.supplier.id,
            'estimated_delivery_date': '2026-12-31',
            # FormSet Management Form fields
            'lines_purchases_order-TOTAL_FORMS': '2',
            'lines_purchases_order-INITIAL_FORMS': '1',
            'lines_purchases_order-MIN_NUM_FORMS': '0',
            'lines_purchases_order-MAX_NUM_FORMS': '1000',
            # Line 0 (modified existing)
            'lines_purchases_order-0-id': line1.id,
            'lines_purchases_order-0-material': self.material1.id,
            'lines_purchases_order-0-quantity': 15,
            'lines_purchases_order-0-unit_material': self.unit.id,
            'lines_purchases_order-0-price': 150,
            'lines_purchases_order-0-currency': self.currency.id,
            # Line 1 (new line added)
            'lines_purchases_order-1-id': '',
            'lines_purchases_order-1-material': self.material2.id,
            'lines_purchases_order-1-quantity': 30,
            'lines_purchases_order-1-unit_material': self.unit.id,
            'lines_purchases_order-1-price': 800,
            'lines_purchases_order-1-currency': self.currency.id,
        }

        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)

        po.refresh_from_db()
        self.assertEqual(str(po.estimated_delivery_date), '2026-12-31')
        self.assertEqual(po.updated_by, self.user)

        lines = LinesPurchasesOrder.objects.filter(purchase_order=po).order_by('position')
        self.assertEqual(lines.count(), 2)

        line1.refresh_from_db()
        self.assertEqual(line1.quantity, 15)
        self.assertEqual(line1.price, 150)
        self.assertEqual(line1.updated_by, self.user)

        new_line = lines[1]
        self.assertEqual(new_line.material, self.material2)
        self.assertEqual(new_line.quantity, 30)
        self.assertEqual(new_line.price, 800)
        self.assertEqual(new_line.created_by, self.user)

    def test_get_detail_purchase_order_view(self):
        po = PurchasesOrder.objects.create(
            supplier=self.supplier,
            estimated_delivery_date=date.today(),
            created_by=self.user
        )
        line1 = LinesPurchasesOrder.objects.create(
            purchase_order=po,
            material=self.material1,
            quantity=5,
            unit_material=self.unit,
            price=100,
            currency=self.currency,
            received_quantity=2,
            position=1,
            created_by=self.user
        )
        line2 = LinesPurchasesOrder.objects.create(
            purchase_order=po,
            material=self.material2,
            quantity=10,
            unit_material=self.unit,
            price=200,
            currency=self.currency,
            received_quantity=10,
            position=2,
            created_by=self.user
        )
        url = reverse('purchases:purchase_detail', kwargs={'pk': po.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], po)
        self.assertEqual(len(response.context['lines_data']), 2)
        # Check totals: 5*100 + 10*200 = 500 + 2000 = 2500
        self.assertEqual(response.context['total_amount'], 2500)
        self.assertEqual(response.context['total_quantity'], 15)
        self.assertEqual(response.context['total_received'], 12)

        self.assertContains(response, self.supplier.name)
        self.assertContains(response, self.material1.name)
        self.assertContains(response, self.material2.name)
        self.assertContains(response, '2500')
        self.assertContains(response, reverse('purchases:purchase_update', kwargs={'pk': po.pk}))
