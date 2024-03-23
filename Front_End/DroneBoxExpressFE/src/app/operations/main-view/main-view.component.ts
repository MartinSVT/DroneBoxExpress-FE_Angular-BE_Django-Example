import { Component } from '@angular/core';
import { AuthStateComponent } from 'src/app/auth-state/auth-state.component';
import { UserMainService } from 'src/app/user/user-main-service.service';

@Component({
  selector: 'app-main-view',
  templateUrl: './main-view.component.html',
  styleUrls: ['./main-view.component.css']
})
export class MainViewComponent {
  constructor(private userService: UserMainService) {
  }
  get isLoggedIn():boolean {
    return this.userService.isLogged;
  }
}
