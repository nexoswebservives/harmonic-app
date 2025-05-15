
import os
from supabase import create_client

# Conecta com as variáveis definidas no secrets.toml do Streamlit
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://fmkgmyifjzrcwlpdphle.supabase.co")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZta2dteWlmanpyY3dscGRwaGxlIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NTkxMzQ5MywiZXhwIjoyMDYxNDg5NDkzfQ.Miq8Cdx-gq187u8ubQQcw7enefZ3itVbrjySAPdBJ2s")

supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
