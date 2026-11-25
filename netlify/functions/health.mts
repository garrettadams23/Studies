import type { Context } from "@netlify/functions"

// GET /.netlify/functions/health
//
// A read-only status endpoint for the deployed site. It answers which deploy
// is serving, in which deploy context, and from which region, so a glance at
// it (or at its invocations under Netlify's Function metrics) confirms that
// the project's functions are live. It makes no outbound requests, reads no
// secrets and stores nothing, so it is safe to call from anywhere.
//
// Function responses are not covered by the [[headers]] rules in
// netlify.toml, which apply to static files only, so the headers this
// response needs are set here.
export default async (req: Request, context: Context) => {
  return Response.json(
    {
      status: "ok",
      site: context.site?.name ?? null,
      deploy: {
        id: context.deploy?.id ?? null,
        context: context.deploy?.context ?? null,
        published: context.deploy?.published ?? null,
      },
      region: context.server?.region ?? null,
      requestId: context.requestId ?? null,
      time: new Date().toISOString(),
    },
    {
      headers: {
        "cache-control": "no-store",
        "x-content-type-options": "nosniff",
      },
    },
  )
}
