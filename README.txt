
�ļ���

	system�ļ��д��һЩĬ������
	
		databases.txt ������е����ݿ�����
		usrs_secret.txt ������е��û���������

	databases�ļ��� ������������ݿ�

��

	main���� �����ܵ����̿���

	tools�� ȫ�������Լ�д�ĺ��� 
		tools.py
			append_string_to_file ��Ϊ�����ļ�ĩβ׷��һ���ַ�����
			write_to_file ��һ���ַ���д��һ���ļ�����
			object_in_file_list ��һ���ַ�����obj���ж��Ƿ���һ���ļ����� ��Ϊ�õ�list��� ���ԽС���list
			get_object_from_file_expend_to_list 
				���һ���ļ�ÿ��ֻ��һ���ַ��� ��ô��������� ���ص����ļ��������ַ�����һ��list 
				��ʽ��������ӵ�[ '1','1','23' ]
			get_object_from_file_append_to_list 
				���һ���ļ�ÿ���ж���ַ��� ��������� ���ص����ļ��������ַ�����һ��list
				��ʽ��������ӵ�[ ['1','1'],['23','fa'] ]
			
	admin�� �Ǿ���Ĳ���
		
		login.py ��½�й�
			secret_check �����û��������Ƿ���ȷ
			login ��½�ж�
			run_script ����Ϊ�ű�����ʱ �û��������뷽ʽ�����в�ͬ 
				�� 1���������û��� 2�������û��� 3���û�������
				�˺�������Ӧ����
		
		drop.py drop�й�����
			drop_database ɾ�����ݿ� ��Ҫɾ���ļ��� ���Ҹ��� system/databases.txt
		
		create.py create�й�����
			 drop_database �������ݿ� ��Ҫ�����ļ��� ���Ҹ��� system/databases.txt

