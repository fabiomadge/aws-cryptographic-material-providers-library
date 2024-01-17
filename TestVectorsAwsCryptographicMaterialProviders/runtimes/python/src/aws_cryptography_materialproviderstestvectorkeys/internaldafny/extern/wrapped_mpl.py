import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import Wrappers

class default__(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__):

  @staticmethod
  def WrappedMaterialProviders(config):  
    import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.client
    import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.config
    import software_amazon_cryptography_materialproviders_internaldafny
    c = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.client.AwsCryptographicMaterialProviders(
      dafny_client=software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(config).value
    )
    import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.shim
    wrapped_client = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.shim.MaterialProvidersShim(c)
    return Wrappers.Result_Success(wrapped_client)

software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__ = default__