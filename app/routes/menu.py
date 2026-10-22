from flask import Blueprint, redirect

menu_bp = Blueprint('menu', __name__)

EXTERNAL_ROUTES = {
    'open_finance': 'https://www.bb.com.br/site/open-finance/',
    'sobre_nos': 'https://www.bb.com.br/site/sobre-nos/#/',
    'minha_privacidade': 'https://www.bb.com.br/site/pra-voce/seguranca/minha-privacidade/',
    'imprensa': 'https://imprensa.bb.com.br/',
    'relacoes_investidores': 'https://ri.bb.com.br/',
    'imoveis': 'https://www.bb.com.br/site/compras-contratacao-e-venda-de-imoveis/',
    'sustentabilidade': 'https://www.bb.com.br/site/sustentabilidade/como-bb-atua/',
    'analises_investimentos': 'https://www.bb.com.br/site/investimentos/analises/',
    'facebook': 'https://www.facebook.com/bancodobrasil',
    'instagram': 'https://www.instagram.com/bancodobrasil/',
    'youtube': 'https://www.youtube.com/bancodobrasil',
    'linkedin': 'https://www.linkedin.com/company/bancodobrasil/',
    'blog_bb': 'https://blog.bb.com.br/',
    'acesso_a_informacao': 'https://www.bb.com.br/site/acesso-a-informacao/',
    'transparencia': 'https://www.bb.com.br/site/portal-da-transparência/',
    'declaracao_acessibilidade': 'https://www.bb.com.br/site/declaracao-de-acessibilidade/',
    'reforma_tributaria': 'https://www.bb.com.br/site/reforma-tributaria/'
}


def _external(key):
    return redirect(EXTERNAL_ROUTES[key])


@menu_bp.route('/o-bb/open-finance')
def redirect_open_finance():
    return _external('open_finance')


@menu_bp.route('/o-bb/sobre-nos')
def redirect_sobre_nos():
    return _external('sobre_nos')


@menu_bp.route('/o-bb/imprensa')
def redirect_imprensa():
    return _external('imprensa')


@menu_bp.route('/o-bb/imoveis')
def redirect_imoveis():
    return _external('imoveis')


@menu_bp.route('/o-bb/sustentabilidade')
def redirect_sustentabilidade():
    return _external('sustentabilidade')


@menu_bp.route('/o-bb/analises-de-investimentos')
def redirect_analises_investimentos():
    return _external('analises_investimentos')


@menu_bp.route('/redes-sociais/facebook')
def redirect_facebook():
    return _external('facebook')


@menu_bp.route('/redes-sociais/instagram')
def redirect_instagram():
    return _external('instagram')


@menu_bp.route('/redes-sociais/youtube')
def redirect_youtube():
    return _external('youtube')


@menu_bp.route('/redes-sociais/linkedin')
def redirect_linkedin():
    return _external('linkedin')


@menu_bp.route('/blog-bb')
def redirect_blog_bb():
    return _external('blog_bb')


@menu_bp.route('/acesso-a-informacao')
def redirect_acesso_a_informacao():
    return _external('acesso_a_informacao')


@menu_bp.route('/transparencia')
def redirect_transparencia():
    return _external('transparencia')


@menu_bp.route('/declaracao-de-acessibilidade')
def redirect_declaracao_acessibilidade():
    return _external('declaracao_acessibilidade')


@menu_bp.route('/reforma-tributaria')
def redirect_reforma_tributaria():
    return _external('reforma_tributaria')
