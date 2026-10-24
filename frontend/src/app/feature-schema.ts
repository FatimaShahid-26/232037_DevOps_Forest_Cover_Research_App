export interface Feature {
  name: string;
  label: string;
  min: number;
  max: number;
  step?: number;
}

export const FEATURES: Feature[] = [
  {
    name: 'Elevation',
    label: 'Elevation (meters)',
    min: 0,
    max: 9000
  },
  {
    name: 'Aspect',
    label: 'Aspect (degrees)',
    min: 0,
    max: 360
  },
  {
    name: 'Slope',
    label: 'Slope (degrees)',
    min: 0,
    max: 90
  },
  {
    name: 'Horizontal_Distance_To_Hydrology',
    label: 'Horizontal distance to water (m)',
    min: 0,
    max: 100000
  },
  {
    name: 'Vertical_Distance_To_Hydrology',
    label: 'Vertical distance to water (m)',
    min: -10000,
    max: 10000
  },
  {
    name: 'Horizontal_Distance_To_Roadways',
    label: 'Distance to roadways (m)',
    min: 0,
    max: 100000
  },
  {
    name: 'Hillshade_9am',
    label: 'Hillshade at 9 AM',
    min: 0,
    max: 255
  },
  {
    name: 'Hillshade_Noon',
    label: 'Hillshade at noon',
    min: 0,
    max: 255
  },
  {
    name: 'Hillshade_3pm',
    label: 'Hillshade at 3 PM',
    min: 0,
    max: 255
  },
  {
    name: 'Horizontal_Distance_To_Fire_Points',
    label: 'Distance to fire points (m)',
    min: 0,
    max: 100000
  }
];