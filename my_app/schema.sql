DROP TABLE IF EXISTS organizacao_ingles;

CREATE TABLE organizacao_ingles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    english_sentence TEXT,
    portuguese_sentence TEXT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);