import { Component, ChangeDetectorRef, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import {
  FormBuilder,
  ReactiveFormsModule,
  Validators
} from '@angular/forms';

import { FEATURES } from './feature-schema';
import {
  PredictionService,
  PredictionResult
} from './prediction.service';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {

  isStaticDeployment =
  window.location.hostname.endsWith('github.io');

  private fb = inject(FormBuilder);
  private predictionService = inject(PredictionService);
  private cdr = inject(ChangeDetectorRef);

  features = FEATURES;

  models = [
    { value: 'decision_tree', label: 'Decision Tree' },
    { value: 'random_forest', label: 'Random Forest' },
    { value: 'knn', label: 'KNN' },
    { value: 'xgboost', label: 'XGBoost' }
  ];

  wildernessOptions = [1, 2, 3, 4];
  soilOptions = Array.from(
    { length: 40 },
    (_, i) => i + 1
  );

  form = this.fb.group({
    model: ['random_forest', Validators.required],

    Elevation: [2800, Validators.required],
    Aspect: [180, Validators.required],
    Slope: [15, Validators.required],

    Horizontal_Distance_To_Hydrology: [
      300, Validators.required
    ],

    Vertical_Distance_To_Hydrology: [
      50, Validators.required
    ],

    Horizontal_Distance_To_Roadways: [
      1000, Validators.required
    ],

    Hillshade_9am: [210, Validators.required],
    Hillshade_Noon: [230, Validators.required],
    Hillshade_3pm: [150, Validators.required],

    Horizontal_Distance_To_Fire_Points: [
      700, Validators.required
    ],

    Wilderness_Area: [1, Validators.required],
    Soil_Type: [10, Validators.required]
  });

  result: PredictionResult | null = null;

  error = '';
  loading = false;

  predict() {

    if (this.isStaticDeployment) {
      this.error =
        'Live predictions are available in the local version of this application. Start the Flask backend and Angular development server to use the trained models.';
      return;
    }

      console.log('Predict button clicked');
      if (this.form.invalid || this.loading) {
        console.log('Form invalid or already loading');
        return;
      }

    if (this.form.invalid || this.loading) {
      this.form.markAllAsTouched();
      return;
    }

    this.loading = true;
    this.error = '';
    this.result = null;

    const values = this.form.getRawValue();

    const {
      model,
      ...rawFeatures
    } = values;

    const features = Object.fromEntries(
      Object.entries(rawFeatures).map(
        ([key, value]) => [key, Number(value)]
      )
    );

    const invalidField = this.features.find(field => {
      const value = features[field.name];
      return (
        !Number.isFinite(value) ||
        value < field.min ||
        value > field.max
      );
    });

    if (invalidField) {
      this.error = `Invalid input: ${invalidField.label}`;
      this.loading = false;
      return;
    }

    this.predictionService.predict(
      model!,
      features
    ).subscribe({
      next: (response) => {
        console.log('Prediction response:', response);

        this.result = response;
        this.loading = false;

        this.cdr.markForCheck();
      },

      error: (err) => {
        console.error('Prediction API error:', err);

        this.error =
          err.error?.error ||
          err.message ||
          'Prediction failed.';

        this.loading = false;

        this.cdr.markForCheck();
      }
    });
  }
}