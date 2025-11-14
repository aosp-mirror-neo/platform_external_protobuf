import unittest
from google.protobuf.internal import (
    any_test,
    decoder_test,
    descriptor_database_test,
    descriptor_pool_test,
    descriptor_test,
    duration_test,
    field_mask_test,
    generator_test,
    import_test,
    json_format_test,
    keywords_test,
    message_factory_test,
    message_test,
    proto_builder_test,
    proto_json_test,
    proto_test,
    reflection_cpp_test,
    reflection_test,
    runtime_version_test,
    service_reflection_test,
    symbol_database_test,
    text_encoding_test,
    text_format_test,
    thread_safe_test,
    timestamp_test,
    unknown_fields_test,
    # Requires zoneinfo, which is currently broken in host Python (missing tzdata)
    # well_known_types_test,
    wire_format_test,
)

class AllTests(unittest.TestSuite):
    def __init__(self):
        super().__init__()
        loader = unittest.defaultTestLoader
        self.addTests([
            loader.loadTestsFromModule(any_test),
            loader.loadTestsFromModule(decoder_test),
            loader.loadTestsFromModule(descriptor_database_test),
            loader.loadTestsFromModule(descriptor_pool_test),
            loader.loadTestsFromModule(descriptor_test),
            loader.loadTestsFromModule(duration_test),
            loader.loadTestsFromModule(field_mask_test),
            loader.loadTestsFromModule(generator_test),
            loader.loadTestsFromModule(import_test),
            loader.loadTestsFromModule(json_format_test),
            loader.loadTestsFromModule(keywords_test),
            loader.loadTestsFromModule(message_factory_test),
            loader.loadTestsFromModule(message_test),
            loader.loadTestsFromModule(proto_builder_test),
            loader.loadTestsFromModule(proto_json_test),
            loader.loadTestsFromModule(proto_test),
            loader.loadTestsFromModule(reflection_cpp_test),
            loader.loadTestsFromModule(reflection_test),
            loader.loadTestsFromModule(runtime_version_test),
            loader.loadTestsFromModule(service_reflection_test),
            loader.loadTestsFromModule(symbol_database_test),
            loader.loadTestsFromModule(text_encoding_test),
            loader.loadTestsFromModule(text_format_test),
            loader.loadTestsFromModule(thread_safe_test),
            loader.loadTestsFromModule(timestamp_test),
            loader.loadTestsFromModule(unknown_fields_test),
            # loader.loadTestsFromModule(well_known_types_test),
            loader.loadTestsFromModule(wire_format_test),
        ])


if __name__ == '__main__':
    # Passing warnings="default" ignores deprecation warnings raised by reflection_test
    runner = unittest.TextTestRunner(verbosity=2, warnings="default")
    runner.run(AllTests())
