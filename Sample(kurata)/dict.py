#-----------------------------------------------------------------
#������ "�i�[����Ă���f�[�^�ɖ��O��t���邱�Ƃň�����e�Ղɂ���"
#-----------------------------------------------------------------

#����(dict)�̍쐬 'key:value'
adrs = {'yamada': 'tokyo', 'kurata': 'saitama', 'saito': 'gunma'}

#�^
print(type(adrs))

#key�̕\��
print(adrs.keys())

#value�̕\��
print(adrs.values())

#(key,value)�̕\��
print(adrs.items())

#value�̎Q��1
print(adrs['yamada'])
print(adrs['kurata'])
print(adrs['saito'])

#value�̎Q��2
for i in adrs:
    print(i,adrs[i])


#value�̕ύX
adrs['yamada']='shizuoka'
print(adrs)

#�Q�l�F�����̒��Ɏ������쐬
books = {
    'title1':
    {
        'author': '���킳�� ����',
        'contents': '�^�v��',
    },
    'title2':
    {
        'author': '��F ���F',
        'contents': 'Deep Learning�R�~���j�e�B�[�c�c',
    },
    'title3':
    {
        'author': '���킳�� ����',
        'contents': '���X�g�̑���',
    }
}

#�����̒��̎����̎Q��
print(books['title2']['author'])

