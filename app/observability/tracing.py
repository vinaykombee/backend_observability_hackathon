from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

def setup_tracing(app):
    FastAPIInstrumentor.instrument_app(app)