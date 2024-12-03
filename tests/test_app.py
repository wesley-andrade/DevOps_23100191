import unittest
from app import app, db, Aluno

class TestCadastroAluno(unittest.TestCase):

    def setUp(self):
        """Cria um ambiente de teste com banco de dados vazio"""
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()  # Cria as tabelas no banco de dados

    def tearDown(self):
        """Limpa o banco de dados após cada teste, mas só exclui o aluno adicionado"""
        with app.app_context():
            # Exclui o aluno específico que foi adicionado no teste
            aluno = Aluno.query.filter_by(ra='123456').first()
            if aluno:
                db.session.delete(aluno)
                db.session.commit()

    def test_adicionar_aluno(self):
        """Testa a funcionalidade de adicionar um aluno"""
        aluno_data = {
            "nome": "João",
            "sobrenome": "Silva",
            "turma": "Turma A",
            "disciplinas": "Matemática, Física",
            "ra": "123456"
        }

        response = self.app.post('/alunos', json=aluno_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Aluno adicionado com sucesso!', response.data)

        # Verifica se o aluno foi adicionado ao banco de dados
        with app.app_context():
            aluno = Aluno.query.filter_by(ra='123456').first()
            self.assertIsNotNone(aluno)
            self.assertEqual(aluno.nome, 'João')
            self.assertEqual(aluno.sobrenome, 'Silva')
            self.assertEqual(aluno.turma, 'Turma A')
            self.assertEqual(aluno.disciplinas, 'Matemática, Física')
            self.assertEqual(aluno.ra, '123456')

if __name__ == '__main__':
    unittest.main()
