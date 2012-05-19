
文件夹

	system文件夹存放一些默认配置
	
		databases.txt 存放已有的数据库名字
		usrs_secret.txt 存放已有的用户名和密码

	databases文件夹 存放真正的数据库

包

	main函数 进行总的流程控制

	tools包 全部都是自己写的函数 
		tools.py
			append_string_to_file 是为了在文件末尾追加一个字符串的
			write_to_file 将一个字符串写到一个文件里面
			object_in_file_list 给一个字符串（obj）判断是否在一个文件里面 因为用的list存的 所以叫、、list
			get_object_from_file_expend_to_list 
				如果一个文件每行只有一个字符串 那么用这个函数 返回的是文件中所有字符串的一个list 
				格式是这个样子的[ '1','1','23' ]
			get_object_from_file_append_to_list 
				如果一个文件每行有多个字符串 用这个函数 返回的是文件中所有字符串的一个list
				格式是这个样子的[ ['1','1'],['23','fa'] ]
			
	admin包 是具体的操作
		
		login.py 登陆有关
			secret_check 检验用户名密码是否正确
			login 登陆判断
			run_script 当做为脚本运行时 用户密码输入方式可能有不同 
				如 1、不输入用户名 2、仅有用户名 3、用户名密码
				此函数做相应处理
		
		drop.py drop有关命令
			drop_database 删除数据库 需要删除文件夹 并且更改 system/databases.txt
		
		create.py create有关命令
			 drop_database 创建数据库 需要创建文件夹 并且更改 system/databases.txt

