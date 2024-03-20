import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-create-new-order',
  templateUrl: './create-new-order.component.html',
  styleUrls: ['./create-new-order.component.css']
})
export class CreateNewOrderComponent {
  constructor(private myFormBuilder: FormBuilder) {}

  newOrderForm = this.myFormBuilder.group({
    route: ['', [Validators.required, ]],
    weight: ['', [Validators.required, Validators.min(0.01)]],
    cost: ['', [Validators.required, Validators.min(0.01)]]
  });
  

  createOrder(): void {
    if (this.newOrderForm.invalid) {
      return;
    }
    console.log(this.newOrderForm.value);
  }

  calculateCost(event: Event, weightVal: any): void {
    event.preventDefault();
    const cost: number = Number(weightVal) * 23
    if (cost <= 0) {
      return
    } 
    this.newOrderForm.get("cost")?.setValue(String(cost))
  }
}
