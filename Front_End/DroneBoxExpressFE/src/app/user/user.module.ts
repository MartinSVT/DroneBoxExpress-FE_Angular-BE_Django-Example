import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { EditComponent } from './edit/edit.component';
import { DeleteComponent } from './delete/delete.component';



@NgModule({
  declarations: [
    LoginComponent,
    RegisterComponent,
    EditComponent,
    DeleteComponent
  ],
// Add Custom Modules if necessary to use their components
  imports: [
    CommonModule,
  ],
  exports: [
    LoginComponent,
    RegisterComponent,
    EditComponent,
    DeleteComponent
  ]
})
export class UserModule { }
