import * as SQLite from 'expo-sqlite';
import { createRepository, Database } from './repository';
const native = SQLite.openDatabaseSync('saber_em_jogo_v1.db');
const adapter: Database = {
 execSync: sql => native.execSync(sql),
 runSync: (sql, params = []) => native.runSync(sql, params),
 getFirstSync: <T>(sql: string, params: (string|number|null)[] = []) => native.getFirstSync<T>(sql, params),
 getAllSync: <T>(sql: string, params: (string|number|null)[] = []) => native.getAllSync<T>(sql, params),
 withTransactionSync: task => native.withTransactionSync(task),
};
export const repository = createRepository(adapter);
