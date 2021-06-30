from django.contrib import admin

# Register your models here.
from .models import *

class sign_data(admin.ModelAdmin):
    list_display=['id','us_first_name','us_last_name','us_email','us_password','us_phone','us_DOB','us_date','us_time']

class user_data(admin.ModelAdmin):
    list_display=['id','u_name','u_password','u_date','u_time','sign_up']

class employee_login_data(admin.ModelAdmin):
    list_display=['id','el_name','el_password','el_date','el_time','user_login']    

class employee_personal_data(admin.ModelAdmin):
    list_display=['id','e_name','e_fathername','e_CNIC','e_DOB','e_gender','e_address','e_city','e_postal_code','e_date','e_time']    

class employee_qualification_data(admin.ModelAdmin):
    list_display=['id','eq_qualification','eq_institute','eq_marks_or_CGPA','eq_subject','eq_board','eq_percentage','eq_reg_no','eq_year','eq_date','eq_time','employee_name']

class employee_skills_data(admin.ModelAdmin):
    list_display=['id','es_skills','es_certification','es_organization','es_year','es_date','es_time','employee_name']

class employee_contact_data(admin.ModelAdmin):
    list_display=['id','ec_phone','ec_email','ec_date','ec_time','employee_name']

class employee_experience_data(admin.ModelAdmin):
    list_display=['id','ee_fresh_or_experienced','ee_designation','ee_organization','ee_joining_date','ee_leaving_date','ee_NOC','ee_leaving_reason','ee_date','ee_time','employee_name']       

class employee_duty_timing_data(admin.ModelAdmin):
    list_display=['id','ed_department','ed_designation','ed_salary','ed_shift','ed_duty_time','ed_vacations','ed_bonus','ed_date','ed_time','employee_name']

class distributer_personal_data(admin.ModelAdmin):
    list_display=['id','d_name','d_address','d_city','d_reg_no','d_fax_no','d_toll_free_no','d_ISO_no','d_postalcode','d_type']

class distributer_contact_data(admin.ModelAdmin):
    list_display=['id','dc_phone','dc_email','dc_date','dc_time','distributer_name']

class distributer_brand_data(admin.ModelAdmin):
    list_display=['id','dbr_name','dbr_type','dbr_description','dbr_manufacturing_detail','dbr_date','dbr_time','distributer_name']

class distributer_professional_data(admin.ModelAdmin):
    list_display=['id','dpr_category','dpr_date','dpr_time','distributer_name']

class distributer_representator_data(admin.ModelAdmin):
    list_display=['id','dr_name','dr_father_name','dr_designation','dr_phone','dr_email','dr_date','dr_time','distributer_name']

class product_personal_data(admin.ModelAdmin):
    list_display=['id','p_name','p_quality','p_color','p_size','p_stuff','brand_name']

class product_professional_data(admin.ModelAdmin):
    list_display=['id','pr_purchase_unit_price','pr_purchase_bulk_price','pr_sale_unit_price','pr_sale_bulk_price','pr_bulk_quantity','pr_date','pr_time','product_name']

class stock_order_booking_data(admin.ModelAdmin):
    list_display=['id', 'sob_invoice_no','sob_total_bill','sob_booking_date','sob_delivery_date','sob_date','sob_time','employee_name','distributer_name']

class current_stock_data(admin.ModelAdmin):
    list_display=['id','cs_product_name','cs_quantity','cs_unit_price','cs_date','cs_time']

class stock_order_detail_data(admin.ModelAdmin):
    list_display=['id','sod_quantity','sod_unit_price','sod_bulk_price','sod_packing_detail','sod_status','product_name','product_purchase_unitprice','stock_invoice','currentstock_product']

class stock_order_payment_data(admin.ModelAdmin):
    list_display=['id','sop_payment','sop_medium','sop_date','sop_time','stock_total_bill','employee_name']

class customer_personal_data(admin.ModelAdmin):
    list_display=['id','c_name','c_phone','c_CNIC','c_email','c_address','c_city','c_postal_code','c_date','c_time']

class customer_order_booking_data(admin.ModelAdmin):
    list_display=['id','cob_total_bill','cob_total_product','cob_invoice_no','cob_booking_date','cob_delivery_date','cob_date','cob_time','customer_name','employee_name']

class customer_order_detail_data(admin.ModelAdmin):
    list_display=['id','cod_product_name','cod_quantity','cod_sale_unit_price','cod_sale_bulk_price','customer_name','product_name','product_sale_unitprice','currentstock_product']

class customer_order_payment_data(admin.ModelAdmin):
    list_display=['id','cop_amount','cop_date','cop_time','total_bill','employee_name']

class expenditure_data(admin.ModelAdmin):
    list_display=['id','ex_type','ex_description','ex_amount','ex_receipt','ex_date','ex_time','employee_name']

class net_income_data(admin.ModelAdmin):
    list_display=['id','n_starting_date','n_ending_date','n_amount_paid','n_amount_received','n_amount_due','employee_name']

class showproduct(admin.ModelAdmin):
    list_display=['id','product_name','product_price','product_image_front','product_image_back','product_date','category']

class arr_dat(admin.ModelAdmin):
    list_display=['id','Collections','Discounts','price','c_image','l_image','l_Discounts','d_image','d_Discounts','s_image','Season','Category','date']    

class arr1_dat(admin.ModelAdmin):
    list_display=['id','M_name','M_price','M_image','M_Discription','W_Discription','W_name','W_price','W_image','S_name','S_price','S_image','date']  

class arr2_dat(admin.ModelAdmin):
    list_display=['id','b_name','b_price','b_image','M_name','M_price','M_image','R_name','R_price','R_image','O_name','O_price','O_image','date']

class arr3_dat(admin.ModelAdmin):
    list_display=['id','name','discription','image','date']

class arr4_dat(admin.ModelAdmin):
    list_display=['id','name','discription','image','date']    

class contact_data(admin.ModelAdmin):
    list_display=['id','name','email','message','date']

class info_data(admin.ModelAdmin):
    list_display=['id','address','city','phone1','phone2','email1','email2','date']

class simple_data(admin.ModelAdmin):
    list_display=['id','login_account','select_item','make_payment','date'] 
  
class carts_data(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

class customer_data(admin.ModelAdmin):
    list_display=['id','user','name','phone','email','address','city','postal_code','state'] 

class OrderItemInLine (admin.TabularInline):
    model = Placed
    raw_id_fields = ['order']
@admin.register(reqq)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [OrderItemInLine]     
      

admin.site.register(sign_up,sign_data)
admin.site.register(userlogin,user_data)
admin.site.register(employee_login,employee_login_data)
admin.site.register(employee_personal,employee_personal_data)
admin.site.register(employee_qualification,employee_qualification_data)
admin.site.register(employee_skills,employee_skills_data)
admin.site.register(employee_contact,employee_contact_data)
admin.site.register(employee_experience,employee_experience_data)
admin.site.register(employee_duty_timing,employee_duty_timing_data)
admin.site.register(distributer_personal,distributer_personal_data)
admin.site.register(distributer_contact,distributer_contact_data)
admin.site.register(distributer_brand,distributer_brand_data)
admin.site.register(distributer_professional,distributer_professional_data)
admin.site.register(distributer_representator,distributer_representator_data)
admin.site.register(product_personal,product_personal_data)
admin.site.register(product_professional,product_professional_data)
admin.site.register(stock_order_booking,stock_order_booking_data)
admin.site.register(current_stock,current_stock_data)
admin.site.register(stock_order_detail,stock_order_detail_data)
admin.site.register(stock_order_payment,stock_order_payment_data)
admin.site.register(customer_personal,customer_personal_data)
admin.site.register(customer_order_booking,customer_order_booking_data)
admin.site.register(customer_order_detail,customer_order_detail_data)
admin.site.register(customer_order_payment,customer_order_payment_data)
admin.site.register(expenditure,expenditure_data)
admin.site.register(net_income,net_income_data)
admin.site.register(product,showproduct)
admin.site.register(arrivals,arr_dat)
admin.site.register(arrivals1,arr1_dat)
admin.site.register(electronic,arr2_dat)
admin.site.register(men,arr3_dat)
admin.site.register(women,arr3_dat)
admin.site.register(contact,contact_data)
admin.site.register(info,info_data)
admin.site.register(simple,simple_data)
admin.site.register(carts,carts_data)
admin.site.register(Customer,customer_data)
