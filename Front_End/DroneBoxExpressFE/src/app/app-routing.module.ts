import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './core/home/home.component';
import { ErrorComponent } from './shared/error/error.component';
import { ContactsComponent } from './core/contacts/contacts.component';
import { AboutUsComponent } from './core/about-us/about-us.component';
import { AddArticleComponent } from './core/add-article/add-article.component';
import { EditArticleComponent } from './core/edit-article/edit-article.component';
import { DeleteArticleComponent } from './core/delete-article/delete-article.component';

const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: '/home' },
  { path: 'home', component: HomeComponent },
  { path: 'contacts', component: ContactsComponent},
  { path: 'about', component: AboutUsComponent},
  { path: 'addArticle', component: AddArticleComponent},
  { path: 'editArticle', component: EditArticleComponent},
  { path: 'deleteArticle', component: DeleteArticleComponent},
  { path: '**', redirectTo: '/404' },
  { path: '404', component: ErrorComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
