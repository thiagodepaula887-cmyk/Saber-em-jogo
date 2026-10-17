import bank from './questions.json';
import {QuizQuestion,validateItem} from '../types/quiz';
const input:unknown=bank;
if(!Array.isArray(input)||!input.every(validateItem)) throw new Error('Banco inicial inválido.');
export const seed:QuizQuestion[]=input;
