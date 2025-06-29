import sqlite3

DB_PATH = 'biblioteca.db'

EMAIL_DO_ADMIN = '4111.fpn@gmail.com' 

def promover_para_admin():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Executa o comando SQL para mudar o 'role' do utilizador
        cursor.execute("UPDATE usuarios SET role = 'admin' WHERE email = ?", (EMAIL_DO_ADMIN,))

        if cursor.rowcount == 0:
            print(f"ERRO: Nenhum utilizador encontrado com o e-mail '{EMAIL_DO_ADMIN}'. Certifica-te de que o e-mail está correto e já foi registado.")
        else:
            conn.commit()
            print(f"Sucesso! O utilizador '{EMAIL_DO_ADMIN}' foi promovido a administrador.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    promover_para_admin()