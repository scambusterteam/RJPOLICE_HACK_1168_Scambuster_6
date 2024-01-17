import { Component, OnInit } from '@angular/core';
import { TokenStorageService } from '../_services/token-storage.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { UserService } from '../_services/user.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  currentUser: any;
  user:any;
  form: FormGroup;
  constructor(private token: TokenStorageService,
    private fb: FormBuilder,
    private userService:UserService) {
    this.form = this.fb.group({
      url: ['', [Validators.required]],
      phone: ['', [Validators.required]],
    });
   }

  ngOnInit(): void {
    this.currentUser = this.token.getUser();
    this.user=this.currentUser['user'];
  }

  onSubmit(type:any)
  {
    if(type==='URL')
    {
      const urlValue = this.form.get('url')?.value;
      if (urlValue) {
        const urlData = { url: urlValue };
  
        this.userService.urlCheck(urlData).subscribe({
          next: data => {
            console.log(data);
            alert(data);
          },
          error: err => {
            console.error(err);
          }
        });
      }
    }
    if(type==='PHONE')
    {
      const phoneValue = this.form.get('phone')?.value;
      if (phoneValue) {
        const phoneData = { url: phoneValue };
  
        this.userService.phoneCheck(phoneData).subscribe({
          next: data => {
            console.log(data);
            alert(data);
          },
          error: err => {
            console.error(err);
          }
        });
      }
    }
  }

}
