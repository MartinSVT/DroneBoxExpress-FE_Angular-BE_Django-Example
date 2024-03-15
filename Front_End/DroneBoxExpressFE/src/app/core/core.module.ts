import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home/home.component';
import { AddArticleComponent } from './add-article/add-article.component';
import { EditArticleComponent } from './edit-article/edit-article.component';
import { DeleteArticleComponent } from './delete-article/delete-article.component';



@NgModule({
  declarations: [
    HomeComponent,
    AddArticleComponent,
    EditArticleComponent,
    DeleteArticleComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
    HomeComponent,
    AddArticleComponent,
    EditArticleComponent,
    DeleteArticleComponent
  ]
})
export class CoreModule { }
