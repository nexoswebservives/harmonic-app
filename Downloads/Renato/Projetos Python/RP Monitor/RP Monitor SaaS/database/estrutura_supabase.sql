
-- Estrutura exemplo para Supabase
CREATE TABLE IF NOT EXISTS profiles (
    id UUID PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    plano TEXT NOT NULL DEFAULT 'Free',
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE IF NOT EXISTS analises (
    id UUID PRIMARY KEY,
    cliente TEXT,
    sentimento TEXT,
    urgencia TEXT,
    fonte TEXT,
    autor TEXT,
    timestamp TIMESTAMP DEFAULT now(),
    usuario_id UUID REFERENCES profiles(id)
);
