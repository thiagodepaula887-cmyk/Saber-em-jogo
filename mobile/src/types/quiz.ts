export const categories = ['esportes','religião','história','geografia','português','matemática','artes','literatura','variedades'] as const;
export type GeneralCategory = typeof categories[number];
export type AppMode = 'oab' | 'geral';
export type OptionIndex = 0 | 1 | 2 | 3;
interface BaseQuestion {
  id: string; version: number; subject: string; statement: string;
  options: [string,string,string,string]; correctAnswer: OptionIndex;
  explanation: string; difficulty: 'fácil' | 'médio' | 'difícil';
}
export interface QuestionOAB extends BaseQuestion {
  discipline: string; origin: 'autoral' | 'prova_anterior'; legalReferences: string[];
}
export interface QuestionGeneral extends BaseQuestion { category: GeneralCategory; }
export type QuizQuestion = { mode: 'oab'; question: QuestionOAB } | { mode: 'geral'; question: QuestionGeneral };
const text = (v: unknown): v is string => typeof v === 'string' && v.trim().length > 0;
const record = (v: unknown): v is Record<string, unknown> => v !== null && typeof v === 'object' && !Array.isArray(v);
export function validateItem(value: unknown): value is QuizQuestion {
  if (!record(value) || !record(value.question)) return false;
  const q = value.question;
  if (![q.id,q.subject,q.statement,q.explanation].every(text)) return false;
  if (!Number.isSafeInteger(q.version) || (q.version as number) < 1) return false;
  if (!Array.isArray(q.options) || q.options.length !== 4 || !q.options.every(text)) return false;
  if (new Set(q.options.map(s => s.trim())).size !== 4) return false;
  if (![0,1,2,3].includes(q.correctAnswer as number)) return false;
  if (!['fácil','médio','difícil'].includes(q.difficulty as string)) return false;
  if (value.mode === 'geral') return categories.includes(q.category as GeneralCategory);
  return value.mode === 'oab' && text(q.discipline) && ['autoral','prova_anterior'].includes(q.origin as string)
    && Array.isArray(q.legalReferences) && q.legalReferences.length > 0 && q.legalReferences.every(text);
}
export function canonical(item: QuizQuestion): string {
  const q = item.question;
  return JSON.stringify({mode:item.mode,question:{id:q.id,version:q.version,subject:q.subject,statement:q.statement,options:q.options,
    correctAnswer:q.correctAnswer,explanation:q.explanation,difficulty:q.difficulty,
    ...(item.mode === 'oab' ? {discipline:item.question.discipline,origin:item.question.origin,legalReferences:item.question.legalReferences}
      : {category:item.question.category})}});
}
