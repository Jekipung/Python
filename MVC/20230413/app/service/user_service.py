import bcrypt

class UserService:

    def __init__(self):
        pass

    def registration(self, user_id, user_pw):
        """
        회원 등록 서비스 함수
        """

        b_user_pw = bytes(user_pw, 'utf-8')
        b_hashed_pw = bcrypt.hashpw(password=b_user_pw, salt=bcrypt.gensalt())

        print('hashed pw:', b_hashed_pw)

