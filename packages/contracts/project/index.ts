/** Planwise Lab project-planner contracts v1.1.0. Framework/runtime independent. */
export const PROJECT_CONTRACT_VERSION = '1.1.0' as const;
export const PROJECT_SCHEMA_VERSION = 2 as const;
export const MAX_TASKS = 200 as const;
export const MAX_DEPENDENCIES = 19900 as const;
export const MAX_CRITICAL_PATHS = 1024 as const;
export const MAX_TASK_DURATION = 1000000 as const;
export const MAX_DATE_HORIZON_DAYS = 1000000 as const;
export const MAX_IMPORT_BYTES = 1048576 as const;
export const MAX_JSON_DEPTH = 16 as const;
export const MAX_AGGREGATE_STRING_BYTES = 262144 as const;
export const MAX_TRAVERSAL_PROPERTIES = 25000 as const;
export const MAX_TASK_NAME_LENGTH = 256 as const;
export const MAX_ID_LENGTH = 128 as const;

export type DurationUnit = 'calendar-day' | 'workday';
export type DurationSpec =
  | { kind: 'fixed'; value: number }
  | { kind: 'pert'; optimistic: number; mostLikely: number; pessimistic: number };
export interface ProjectTask { id: string; name: string; duration: DurationSpec; }
export interface Dependency { predecessorId: string; successorId: string; }
export interface ProjectCalendar {
  unit: DurationUnit;
  referenceDate: string;
  timezone: string;
  workingWeekdays: number[]; // 0=Sunday ... 6=Saturday
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
/** Numeric finish values are exclusive elapsed offsets. Displayed finishOffset/date identify the last occupied date; zero duration displays at its start. */
export interface ScheduleEntry {
  taskId: string; duration: number; startOffset: number; finishOffset: number;
  startDate: string; finishDate: string; earliestStart: number; earliestFinish: number;
  latestStart: number; latestFinish: number; float: number; critical: boolean;
}
export interface CriticalPathSummary { paths: string[][]; truncated: boolean; totalPathCount: string; }
export interface ProjectResult {
  contractVersion: typeof PROJECT_CONTRACT_VERSION;
  status: 'ok';
  duration: number; durationUnit: DurationUnit; projectStartDate: string; projectFinishDate: string;
  schedule: ScheduleEntry[]; criticalPaths: CriticalPathSummary;
  pertExpectedDurations: Record<string, number>; warnings: string[];
  deadline?: { deadline: string; feasible: boolean; finishDate: string };
}
export type ProjectErrorCode =
  | 'SCHEMA_VALIDATION_ERROR' | 'UNSUPPORTED_VERSION' | 'UNKNOWN_FIELD' | 'IMPORT_TOO_LARGE'
  | 'IMPORT_TOO_DEEP' | 'IMPORT_STRING_BUDGET_EXCEEDED' | 'IMPORT_TRAVERSAL_BUDGET_EXCEEDED'
  | 'DUPLICATE_TASK_ID' | 'MISSING_TASK_ID' | 'MISSING_PREDECESSOR' | 'MISSING_SUCCESSOR'
  | 'INVALID_DURATION' | 'INVALID_PERT_ORDER' | 'CYCLE_DETECTED' | 'INVALID_DATE'
  | 'INVALID_CALENDAR' | 'DEADLINE_INFEASIBLE' | 'DURATION_HORIZON_EXCEEDED';
export interface ProjectError { code: ProjectErrorCode; message: string; path?: string; taskIds?: string[]; }
export type ProjectResponse = { ok: true; result: ProjectResult } | { ok: false; error: ProjectError };
export interface ProjectPlanner { calculate(input: ProjectInput): ProjectResponse; }
export interface ProjectWorkspaceEnvelope {
  format: 'planwise-workspace'; schemaVersion: typeof PROJECT_SCHEMA_VERSION;
  tool: 'project'; savedAt: string; payload: ProjectInput;
}
export interface ProjectFixture { id: string; description: string; input: ProjectInput; expected: ProjectResponse; }
