import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CreateNewOrderComponent } from './create-new-order/create-new-order.component';
import { EditOrderComponent } from './edit-order/edit-order.component';
import { DeleteOrderComponent } from './delete-order/delete-order.component';
import { ViewOrderComponent } from './view-order/view-order.component';
import { ListOrdersComponent } from './list-orders/list-orders.component';
import { StaffListOrdersComponent } from './staff-list-orders/staff-list-orders.component';



@NgModule({
  declarations: [
    CreateNewOrderComponent,
    EditOrderComponent,
    DeleteOrderComponent,
    ViewOrderComponent,
    ListOrdersComponent,
    StaffListOrdersComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
    CreateNewOrderComponent,
    EditOrderComponent,
    DeleteOrderComponent,
    ViewOrderComponent,
    ListOrdersComponent,
    StaffListOrdersComponent
  ]
})
export class OrdersModule { }
