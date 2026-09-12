import type { ProjectFixture, ProjectInput, ProjectPlanner, ProjectResponse } from './index';

/** Explicit fixture adapter. It never schedules; it only returns a stored fixture result. */
export class MockProjectPlanner implements ProjectPlanner {
  public readonly kind = 'mock' as const;
  private readonly fixtures: readonly ProjectFixture[];

  constructor(fixtures: readonly ProjectFixture[]) { this.fixtures = fixtures; }

  calculate(input: ProjectInput): ProjectResponse {
    const match = this.fixtures.find((fixture) => JSON.stringify(fixture.input) === JSON.stringify(input));
    if (!match) {
      return { ok: false, error: { code: 'SCHEMA_VALIDATION_ERROR', message: 'Mock fixture not found for supplied input.' } };
    }
    return structuredClone(match.expected);
  }
}
