/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { Skill } from './Skill';

export type MemberOut = {
    name: string;
    backstory?: (string | null);
    role: string;
    type: string;
    owner_of: (number | null);
    position_x: number;
    position_y: number;
    source?: (number | null);
    provider?: string;
    model?: string;
    temperature?: number;
    id: number;
    belongs_to: number;
    skills: Array<Skill>;
};
