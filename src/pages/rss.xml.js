import rss, { pagesGlobToRssItems } from '@astrojs/rss';

// Docs: https://docs.astro.build/en/guides/rss/
export async function get() {
    return rss({
        title: 'Engineering Kiosk',
        description: 'Der deutschsprachige Software-Engineering-Podcast mit Wolfgang Gassler und Andy Grunwald rund um die Themen Engineering-Kultur, Open Source und Technologie.',
        site: import.meta.env.SITE,
        items: await pagesGlobToRssItems(import.meta.glob(['./blog/post/*.mdx', './podcast/episode/*.md'])),
        customData: `<language>de-de</language>`,
    });
}