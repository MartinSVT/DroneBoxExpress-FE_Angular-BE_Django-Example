import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListOrdersComponent } from './list-orders/list-orders.component';
import { StaffListOrdersComponent } from './staff-list-orders/staff-list-orders.component';
import { CreateNewOrderComponent } from './create-new-order/create-new-order.component';

const routes: Routes = [
    { path: 'orders', component: ListOrdersComponent},
    { path: 'addOrder', component: CreateNewOrderComponent},
    { path: 'staffOrders', component: StaffListOrdersComponent},
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class OrderRoutingModule {}