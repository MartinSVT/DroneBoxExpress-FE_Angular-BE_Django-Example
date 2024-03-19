import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { matchPassVal } from 'src/app/shared/passMatchValidator';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  constructor(private myFormBuilder: FormBuilder) {}

  regForm = this.myFormBuilder.group({
    username: ['', [Validators.required, Validators.minLength(2)]],
    email: ['', [Validators.required, Validators.email]],
    firstName: ['', [Validators.required, Validators.minLength(2)]],
    lastName: ['', [Validators.required, Validators.minLength(2)]],
    passGroup: this.myFormBuilder.group(
      {
        password1: ['', [Validators.required]],
        password2: ['', [Validators.required]],
      },
      {
        validators: [matchPassVal('password1', 'password2')],
      }
    ),
  });
  
  get passGroup() {
    return this.regForm.get('passGroup');
  }

  register(): void {
    if (this.regForm.invalid) {
      return;
    }
    console.log(this.regForm.value);
  }
}
