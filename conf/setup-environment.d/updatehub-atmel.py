def __after_init_updatehub_atmel():
    PLATFORM_ROOT_DIR = os.environ['PLATFORM_ROOT_DIR']

    append_layers([ os.path.join(PLATFORM_ROOT_DIR, 'sources', p) for p in
                    [
                        'meta-atmel',
                        'meta-updatehub-atmel',
                    ]])

run_after_init(__after_init_updatehub_atmel)
