from django.urls import path
from django.conf.urls import url

from backend.djangoapps.user.auth import views as authViews
from backend.djangoapps.user.board import views as boardViews
from backend.djangoapps.user.company import views as companyViews
from backend.djangoapps.user.helpdesk import views as helpdeskViews
from backend.djangoapps.user.point import views as pointViews
from backend.djangoapps.user.shop import views as shopViews
from backend.djangoapps.user.deposit import views as depositViews
from backend.djangoapps.user.withdrawal import views as withdrawalViews


urlpatterns = [
    # 로그인
    path('signin', authViews.signin, name='signin'), 

    # 회원가입
    path('signup', authViews.signup, name='signup'), 

    # 아이디찾기
    path('find_id', authViews.find_id, name='find_id'),

    # 비밀번호찾기
    path('find_pw', authViews.find_pw, name='find_pw'), 

    # 비밀번호 변경
    path('change_password', authViews.change_password, name='change_password'), 

    # 회원 상세
    path('my/detail', authViews.user_detail, name='user_detail'), 

    # 보유 포인트
    path('my/point', authViews.my_point, name='my_point'), 


    # url 파라미터 분기
    # notification - 공지사항
    # news - 뉴스

    # 게시판 리스트
    path('board/list', boardViews.board_list, name='board_list'), 

    # 게시판 상세
    path('board/detail', boardViews.board_detail, name='board_detail'), 


    # 1:1 문의 리스트
    path('helpdesk/list', helpdeskViews.helpdesk_list, name='helpdesk_list'), 

    # 1:1 문의 상세
    path('helpdesk/detail', helpdeskViews.helpdesk_detail, name='helpdesk_detail'), 

    # 1:1 문의 상세
    path('helpdesk/write', helpdeskViews.helpdesk_write, name='helpdesk_write'), 


    # 쇼핑몰 리스트
    path('shop/list', shopViews.shop_list, name='shop_list'), 

    # 쇼핑몰 상세
    path('shop/detail', shopViews.shop_detail, name='shop_detail'), 

    # 상품 구매하기
    path('shop/buy', shopViews.shop_buy, name='shop_buy'), 

    # 상품 장바구니 담기
    path('shop/add_cart', shopViews.shop_add_cart, name='shop_add_cart'), 

    # 장바구니 리스트
    path('shop/cart_list', shopViews.shop_cart_list, name='shop_cart_list'), 

    # 구매내역
    path('shop/history_list', shopViews.shop_history_list, name='shop_history_list'), 


    # url 파라미터 분기
    # info - 회사소개
    # ecommerce - 전자상거래표준약관
    # account - 회원약관
    # private - 개인정보취급방침
    # clean - 클린젬마인의서약

    # 회사 공통 조회 
    path('company_read/<type>', companyViews.company_read, name='company_read'),    

    # 배너 리스트
    path('banner/list', companyViews.banner_list, name='banner_list'), 


    # 입금정보
    path('deposit/info', depositViews.deposit_info, name='deposit_info'), 

    # 입금확인요청
    path('deposit/request', depositViews.deposit_request, name='deposit_request'), 


    # 출금신청
    path('withdrawal/request', withdrawalViews.withdrawal_request, name='withdrawal_request'), 

    # 출금내역
    path('withdrawal/list', withdrawalViews.withdrawal_list, name='withdrawal_list'), 
]