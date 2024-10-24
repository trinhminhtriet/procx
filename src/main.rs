use anyhow::Result;
use clap::Parser;
use procx::args::CliArgs;
use procx::settings::AppSettings;
use procx::tui::start_app;

fn main() -> Result<()> {
    let config = procx::config::load_app_config()?;
    let args = CliArgs::parse();

    let settings = AppSettings::from(config, &args);
    start_app(args.query, settings)
}
