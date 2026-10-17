export const schema = `
CREATE TABLE IF NOT EXISTS questions (
 id TEXT NOT NULL, version INTEGER NOT NULL CHECK(version>0), mode TEXT NOT NULL CHECK(mode IN ('oab','geral')),
 category TEXT NOT NULL, correct_answer INTEGER NOT NULL CHECK(correct_answer BETWEEN 0 AND 3), payload TEXT NOT NULL,
 PRIMARY KEY(id,version));
CREATE TABLE IF NOT EXISTS question_options (
 question_id TEXT NOT NULL, question_version INTEGER NOT NULL, option_index INTEGER NOT NULL CHECK(option_index BETWEEN 0 AND 3), option_text TEXT NOT NULL CHECK(length(trim(option_text))>0),
 PRIMARY KEY(question_id,question_version,option_index), FOREIGN KEY(question_id,question_version) REFERENCES questions(id,version));
CREATE TABLE IF NOT EXISTS question_references (
 question_id TEXT NOT NULL, question_version INTEGER NOT NULL, position INTEGER NOT NULL, reference_text TEXT NOT NULL,
 PRIMARY KEY(question_id,question_version,position), FOREIGN KEY(question_id,question_version) REFERENCES questions(id,version));
CREATE TABLE IF NOT EXISTS sessions (id TEXT PRIMARY KEY NOT NULL, finished INTEGER NOT NULL DEFAULT 0 CHECK(finished IN(0,1)), created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS session_questions (
 session_id TEXT NOT NULL REFERENCES sessions(id), position INTEGER NOT NULL, question_id TEXT NOT NULL, question_version INTEGER NOT NULL,
 PRIMARY KEY(session_id,position), UNIQUE(session_id,question_id), UNIQUE(session_id,question_id,question_version),
 FOREIGN KEY(question_id,question_version) REFERENCES questions(id,version));
CREATE TABLE IF NOT EXISTS answers (
 session_id TEXT NOT NULL, question_id TEXT NOT NULL, question_version INTEGER NOT NULL, selected_option INTEGER NOT NULL CHECK(selected_option BETWEEN 0 AND 3),
 is_correct INTEGER NOT NULL CHECK(is_correct IN(0,1)), answered_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
 PRIMARY KEY(session_id,question_id), FOREIGN KEY(session_id,question_id,question_version) REFERENCES session_questions(session_id,question_id,question_version));
CREATE INDEX IF NOT EXISTS answers_question ON answers(question_id,question_version);
PRAGMA user_version = 1;
`;
