# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblBanner(models.Model):
    file_id = models.IntegerField(blank=True, null=True)
    banner_desc = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField()
    display_yn = models.CharField(max_length=10, blank=True, null=True)
    delete_yn = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_banner'


class TblBoard(models.Model):
    type = models.CharField(max_length=255)
    sub_type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    user_id = models.IntegerField()
    delete_yn = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_board'


class TblBuyHistory(models.Model):
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    buy_count = models.IntegerField()
    user_id = models.IntegerField()
    status = models.CharField(max_length=10, blank=True, null=True)
    request_date = models.DateTimeField(blank=True, null=True)
    complete_date = models.DateTimeField(blank=True, null=True)
    reject_date = models.DateTimeField(blank=True, null=True)
    cancel_date = models.DateTimeField(blank=True, null=True)
    refund_date = models.DateTimeField(blank=True, null=True)
    delete_yn = models.CharField(max_length=10, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_buy_history'


class TblCode(models.Model):
    group_code = models.CharField(primary_key=True, max_length=255)
    code = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255)
    code_desc = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_code'
        unique_together = (('group_code', 'code'),)


class TblCompany(models.Model):
    type = models.CharField(primary_key=True, max_length=255)
    content = models.TextField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_company'


class TblFile(models.Model):
    type = models.CharField(max_length=255)
    type_id = models.IntegerField(blank=True, null=True)
    file_name = models.CharField(max_length=255)
    file_ext = models.CharField(max_length=255, blank=True, null=True)
    enc_file_name = models.CharField(max_length=255)
    file_raw_size = models.IntegerField()
    file_size = models.CharField(max_length=255)
    save_path = models.CharField(max_length=255)
    user_id = models.IntegerField()
    delete_yn = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_file'


class TblGroupCode(models.Model):
    group_code = models.CharField(primary_key=True, max_length=255)
    group_name = models.CharField(max_length=255)
    group_desc = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_group_code'


class TblHelpdesk(models.Model):
    type = models.CharField(max_length=255)
    sub_type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    user_id = models.IntegerField()
    reply_content = models.TextField()
    status = models.CharField(max_length=10, blank=True, null=True)
    delete_yn = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_helpdesk'


class TblLevel(models.Model):
    level_code = models.CharField(primary_key=True, max_length=255)
    point_rate = models.IntegerField()
    condition_a = models.IntegerField()
    condition_b = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_level'


class TblPointHistory(models.Model):
    type = models.CharField(max_length=10)
    point_type = models.CharField(max_length=10)
    point = models.IntegerField()
    from_user_id = models.IntegerField(blank=True, null=True)
    to_user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_point_history'


class TblProduct(models.Model):
    category = models.CharField(max_length=10, blank=True, null=True)
    thumbnail = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=255)
    product_desc = models.CharField(max_length=255)
    product_content = models.CharField(max_length=255)
    product_refund = models.CharField(max_length=255)
    product_price = models.IntegerField()
    user_id = models.IntegerField()
    display_yn = models.CharField(max_length=10, blank=True, null=True)
    delete_yn = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product'


class TblProductOption(models.Model):
    product_id = models.IntegerField()
    option_name = models.CharField(max_length=255)
    option_price = models.IntegerField()
    option_count = models.IntegerField()
    user_id = models.IntegerField()
    display_yn = models.CharField(max_length=10, blank=True, null=True)
    delete_yn = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_option'


class TblRegistPrice(models.Model):
    price = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_regist_price'


class TblShopCart(models.Model):
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    buy_count = models.IntegerField()
    user_id = models.IntegerField()
    buy_yn = models.CharField(max_length=10, blank=True, null=True)
    delete_yn = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_shop_cart'


class TblUsers(models.Model):
    account = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    birth = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    bank_type = models.CharField(max_length=255, blank=True, null=True)
    bank_number = models.CharField(max_length=255, blank=True, null=True)
    rec_user_id = models.IntegerField(blank=True, null=True)
    a_user_id = models.IntegerField(blank=True, null=True)
    b_user_id = models.IntegerField(blank=True, null=True)
    a_cnt = models.IntegerField(blank=True, null=True)
    b_cnt = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    pin_number = models.CharField(max_length=255, blank=True, null=True)
    is_staff = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    request_date = models.DateTimeField(blank=True, null=True)
    complete_date = models.DateTimeField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    recycle_point = models.IntegerField(blank=True, null=True)
    jnc_point = models.IntegerField(blank=True, null=True)
    delete_yn = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_users'
