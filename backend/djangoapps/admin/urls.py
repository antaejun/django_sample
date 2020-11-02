from django.urls import path
from django.conf.urls import url

from backend.djangoapps.admin.auth import views as authViews
from backend.djangoapps.admin.banner import views as bannerViews
from backend.djangoapps.admin.board import views as boardViews
from backend.djangoapps.admin.company import views as companyViews
from backend.djangoapps.admin.helpdesk import views as helpdeskViews
from backend.djangoapps.admin.point import views as pointViews
from backend.djangoapps.admin.shop import views as shopViews
from backend.djangoapps.admin.system import views as systemViews
from backend.djangoapps.admin.user import views as userViews


urlpatterns = [

    # 로그인
    path('signin', authViews.signin, name='signin'), 


    # 배너 리스트
    path('banner/list', bannerViews.banner_list, name='banner_list'), 

    # 배너 생성
    path('banner/create', bannerViews.banner_create, name='banner_create'), 

    # 배너 수정
    path('banner/update', bannerViews.banner_update, name='banner_update'), 

    # 배너 삭제
    path('banner/delete', bannerViews.banner_delete, name='banner_delete'), 

    # 배너 전시
    path('banner/display', bannerViews.banner_display, name='banner_display'), 


    # 회원 리스트
    path('user/list', userViews.user_list, name='user_list'), 

    # 회원 생성
    path('user/create', userViews.user_create, name='user_create'), 

    # 회원 수정
    path('user/update', userViews.user_update, name='user_update'), 

    # 회원 계보도
    path('user/matrix', userViews.user_matrix, name='user_matrix'), 


    # 관리자 관점의 네이밍
    # give - 지급 ( 관리자 -> 사용자 )
    # collect - 회수 ( 사용자 -> 관리자)

    # 마일리지 지급
    path('give/mileage', pointViews.give_mileage, name='give_mileage'), 

    # 마일리지 회수
    path('collect/mileage', pointViews.collect_mileage, name='collect_mileage'), 

    # 재사용 마일리지 지급
    path('give/recycle_mileage', pointViews.give_recycle_mileage, name='give_recycle_mileage'), 

    # 재사용 마일리지 회수
    path('collect/recycle_mileage', pointViews.collect_recycle_mileage, name='collect_recycle_mileage'), 

    # JNC 지급
    path('give/jnc', pointViews.give_jnc, name='give_jnc'), 

    # JNC 회수
    path('collect/jnc', pointViews.collect_jnc, name='collect_jnc'), 

    # 포인트 사용 내역
    path('point/history', pointViews.point_history, name='point_history'), 


    # 쇼핑몰 리스트
    path('shop/list', shopViews.shop_list, name='shop_list'), 

    # 쇼핑몰 상세
    path('shop/detail', shopViews.shop_detail, name='shop_detail'), 

    # 상품 생성
    path('shop/create', shopViews.shop_create, name='shop_create'), 

    # 상품 수정
    path('shop/update', shopViews.shop_update, name='shop_update'), 

    # 상품 전시
    path('shop/display', shopViews.shop_display, name='shop_display'), 

    # 상품 옵션 전시
    path('shop/option_display', shopViews.shop_option_display, name='shop_option_display'), 

    # 상품 구매 내역
    path('shop/history', shopViews.shop_history, name='shop_history'), 

    # 장바구니 리스트
    path('cart/list', shopViews.cart_list, name='cart_list'), 


    # url 파라미터 분기
    # notification - 공지사항
    # news - 뉴스

    # 게시판 리스트
    path('board_list/<type>', boardViews.board_list, name='board_list'), 

    # 게시판 생성
    path('board_create/<type>', boardViews.board_create, name='board_create'), 

    # 게시판 수정
    path('board_update/<type>', boardViews.board_update, name='board_update'), 

    # 게시판 삭제
    path('board_delete/<type>', boardViews.board_delete, name='board_delete'), 


    # 문의 리스트
    path('helpdesk/list', helpdeskViews.helpdesk_list, name='helpdesk_list'), 

    # 문의 상세
    path('helpdesk/detail', helpdeskViews.helpdesk_detail, name='helpdesk_detail'), 

    # 문의 답장
    path('helpdesk/reply', helpdeskViews.helpdesk_reply, name='helpdesk_reply'),    

    # 문의 거절
    path('helpdesk/reject', helpdeskViews.helpdesk_reject, name='helpdesk_reject'),    


    # url 파라미터 분기
    # info - 회사소개
    # ecommerce - 전자상거래표준약관
    # account - 회원약관
    # private - 개인정보취급방침
    # clean - 클린젬마인의서약

    # 회사 공통 조회 
    path('company_read/<type>', companyViews.company_read, name='company_read'),    

    # 회사 공통 수정
    path('company_update/<type>', companyViews.company_update, name='company_update'),    


    # 직급 리스트
    path('level/list', systemViews.level_list, name='level_list'),    

    # 직급 수정
    path('level/update', systemViews.level_update, name='level_update'),    

    # 회원가입비 조회
    path('regist/read', systemViews.regist_read, name='regist_read'),    

    # 회원가입비 수정
    path('regist/update', systemViews.regist_update, name='regist_update'),    
    
]