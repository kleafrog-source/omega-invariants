export type Coordinates = {
  A: number;
  S: number;
  T: number;
  E: number;
};

export type OperatorDefinition = {
  internal_id: string;
  ascii_key: string;
  display_symbol: string;
  label: string;
  color: string;
  phase_index: number;
};

export type PhaseMatch = {
  operator_id: string;
  display_symbol: string;
  source_text: string;
  start_offset: number | null;
  end_offset: number | null;
  confidence: number;
  synthetic: boolean;
  markers: string[];
};

export type PaletteItem = {
  operator_id: string;
  symbol: string;
  value: string;
  coordinates: Coordinates;
  confidence: number;
  synthetic: boolean;
};

export type ValidationReport = {
  A1_monotonic_path: boolean;
  A2_zero_flux: boolean;
  A3_recurrent_closure: boolean;
  A4_operator_isomorphism: boolean;
  A5_adaptive_density: boolean;
  messages: string[];
};

export type OmegaResult = {
  sequence: string[];
  palette: PaletteItem[];
  phase_matches: PhaseMatch[];
  coordinates: Coordinates[];
  D_metric: number;
  rho_values: number[];
  stability_flag: boolean;
  corrections_applied: string[];
  validation: ValidationReport;
};

export type AnalyzeResponse = {
  result: OmegaResult;
};

export type OperatorsResponse = {
  operators: OperatorDefinition[];
};
