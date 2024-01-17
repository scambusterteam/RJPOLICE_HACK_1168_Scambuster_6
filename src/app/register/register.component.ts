import { Component, OnInit } from '@angular/core';
import { AuthService } from '../_services/auth.service';
import { FormBuilder,FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  form: FormGroup;
  isSuccessful = false;
  isSignUpFailed = false;
  errorMessage = '';
  constructor(private fb: FormBuilder,
    private authService: AuthService) {
    this.form = this.fb.group({
      username: ['', [Validators.required, Validators.minLength(3), Validators.maxLength(20)]],
      email: ['', [Validators.required, Validators.email]],
      phone: ['', [Validators.required, Validators.minLength(10),Validators.pattern(/^[6789]\d{9}$/)]],
      password: ['', [Validators.required, Validators.minLength(6),Validators.pattern(/^(?=.*[a-zA-Z])(?=.*\d).{8,}$/)]],
    });
  }
  ngOnInit(): void {
  }

  onSubmit() {
    debugger
    if (this.form.valid) {
      this.authService.register(this.form.value).subscribe({
        next: data => {
          console.log(data);
          this.isSuccessful = true;
          this.isSignUpFailed = false;
          alert("user registered successfully");
        },
        error: err => {
          this.errorMessage = err.error.message;
          this.isSignUpFailed = true;
        }
      });
    }
  }
}
