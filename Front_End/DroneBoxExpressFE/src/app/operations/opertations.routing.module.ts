import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AirportAddComponent } from './airport-add/airport-add.component';
import { RouteAddComponent } from './route-add/route-add.component';
import { MainViewComponent } from './main-view/main-view.component';

const routes: Routes = [
    { path: 'operations', component: MainViewComponent},
    { path: 'addAirport', component: AirportAddComponent },
    { path: 'addRoute', component: RouteAddComponent },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class OperationsRoutingModule {}