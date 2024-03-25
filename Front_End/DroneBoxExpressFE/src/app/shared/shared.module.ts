import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoaderComponent } from './loader/loader.component';
import { ErrorComponent } from './error/error.component';
import { RouterModule } from '@angular/router';
import { LoingFailureComponent } from './loing-failure/loing-failure.component';



@NgModule({
  declarations: [
    LoaderComponent,
    ErrorComponent,
    LoingFailureComponent
  ],
  imports: [
    CommonModule,
    RouterModule,
  ],
  exports: [
    LoaderComponent,
    ErrorComponent,
    LoingFailureComponent
  ]
})
export class SharedModule { }
