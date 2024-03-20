import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-airport-add',
  templateUrl: './airport-add.component.html',
  styleUrls: ['./airport-add.component.css']
})
export class AirportAddComponent {

  constructor(private myFormBuilder: FormBuilder) {}
  newAirportForm = this.myFormBuilder.group({
    name: ['', [Validators.required, Validators.minLength(2) ]],
    lon: ['', [Validators.required, Validators.pattern("-?[0-9]*\\.?[0-9]+")]],
    lat: ['', [Validators.required, Validators.pattern("-?[0-9]*\\.?[0-9]+")]]
  });
  
  createAirport(): void {
    if (this.newAirportForm.invalid) {
      return;
    }
    console.log(this.newAirportForm.value);
  }
}
