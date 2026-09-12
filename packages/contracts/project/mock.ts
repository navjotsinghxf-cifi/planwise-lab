import type { ProjectFixture, ProjectInput, ProjectPlanner, ProjectResponse } from './index';
export class MockProjectPlanner implements ProjectPlanner {
  public readonly kind = 'mock' as const;
  constructor(private readonly fixtures: readonly ProjectFixture[]) {}
  calculate(input: ProjectInput): ProjectResponse {
    const match = this.fixtures.find((f) => JSON.stringify(f.input) === JSON.stringify(input));
    if (!match) return { ok:false, error:{code:'SCHEMA_VALIDATION_ERROR', message:'Mock fixture not found for supplied input.'} };
    return structuredClone(match.expected);
  }
}
