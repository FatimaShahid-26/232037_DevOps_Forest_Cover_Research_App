import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export interface PredictionResult {
  model: string;
  prediction: number;
  cover_name: string;
  confidence: number;
  probabilities: Record<string, number>;
  disclaimer: string;
}

@Injectable({
  providedIn: 'root'
})
export class PredictionService {
  private http = inject(HttpClient);

  predict(
    model: string,
    features: Record<string, number>
  ) {
    return this.http.post<PredictionResult>(
      '/api/predict',
      {
        model,
        features
      }
    );
  }
}