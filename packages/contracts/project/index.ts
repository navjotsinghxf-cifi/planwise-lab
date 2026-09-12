/** Planwise Lab project-planner contracts v1.0.0. Framework/runtime independent. */
export const PROJECT_CONTRACT_VERSION = '1.0.0' as const;
export const PROJECT_SCHEMA_VERSION = 1 as const;

export type DurationUnit = 'calendar-day' | 'workday';
export type DurationSpec =
  | { kind: 'fixed'; value: number }
  | { kind: 'pert'; optimistic: number; mostLikely: number; pessimistic: number };

export interface ProjectTask {
  id: string;
  name: string;
  duration: DurationSpec;
}
export interface Dependency { predecessorId: string; successorId: string; }
export interface ProjectCalendar {
  unit: DurationUnit;
  referenceDate: string;
  timezone: string;
  workingWeekdays: number[];
  nonWorkingDates: string[];
}
export interface ProjectOptions {
  calculatePertExpectedDuration: boolean;
  checkDeadline: boolean;
  deadline?: string;
}
export interface ProjectInput {
  contractVersion: typeof PROJECT_CONTRACT_VERSION;
  tasks: ProjectTask[];
  dependencies: Dependency[];
  calendar: ProjectCalendar;
  options: ProjectOptions;
}

export interface ScheduleEntry {
  taskId: string;
  duration: number;
  startOffset: number;
  finishOffset: number;
  startDate: string;
  finishDate: string;
  earliestStart: number;
  earliestFinish: number;
  latestStart: number;
  latestFinish: number;
  float: number;
  critical: boolean;
}
export interface ProjectResult {
  contractVersion: typeof PROJECT_CONTRACT_VERSION;
  status: 'ok' | 'invalid-input' | 'cycle' | 'impossible-schedule';
  duration: number;
  durationUnit: DurationUnit;
  projectStartDate: string;
  projectFinishDate: string;
  schedule: ScheduleEntry[];
  criticalPaths: string[][];
  pertExpectedDurations: Record<string, number>;
  warnings: string[];
  deadline?: { deadline: string; feasible: boolean; finishDate: string };
}

export type ProjectErrorCode =
  | 'SCHEMA_VALIDATION_ERROR' | 'DUPLICATE_TASK_ID' | 'MISSING_TASK_ID'
  | 'MISSING_PREDECESSOR' | 'MISSING_SUCCESSOR' | 'INVALID_DURATION'
  | 'INVALID_PERT_ORDER' | 'CYCLE_DETECTED' | 'INVALID_DATE'
  | 'INVALID_CALENDAR' | 'DEADLINE_INFEASIBLE';
export interface ProjectError {
  code: ProjectErrorCode;
  message: string;
  path?: string;
  taskIds?: string[];
}
export type ProjectResponse =
  | { ok: true; result: ProjectResult }
  | { ok: false; error: ProjectError };

export interface ProjectPlanner {
  calculate(input: ProjectInput): ProjectResponse;
}

export interface ProjectWorkspaceEnvelope {
  format: 'planwise-workspace';
  schemaVersion: 1;
  tool: 'project';
  savedAt: string;
  payload: ProjectInput;
}

export interface ProjectFixture {
  id: string;
  description: string;
  input: ProjectInput;
  expected: ProjectResponse;
}
