from .views import ProdutoViewSet, FornecedorViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
#caminho para abrir a lista de produtos na url( nesse caso api/ do arquivo urls do projeto + produtos do router)
router.register('produtos', ProdutoViewSet)
router.register('fornecedores', FornecedorViewSet)