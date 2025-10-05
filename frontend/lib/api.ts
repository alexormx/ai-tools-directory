const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';

async function safeJson(res: Response) {
  try { return await res.json(); } catch { return null; }
}

export async function getTools() {
  try {
    const res = await fetch(`${API_BASE}/api/tools/`, { next: { revalidate: 3600 } });
    if (!res.ok) return { results: [] };
    return await safeJson(res);
  } catch { return { results: [] }; }
}

export async function getToolSlugs(): Promise<string[]> {
  const data = await getTools();
  return (data?.results || []).map((t: any) => t.slug).filter(Boolean).slice(0, 50); // limitar mientras no hay backend
}

export async function getToolDetail(slug: string) {
  try {
    const res = await fetch(`${API_BASE}/api/tools/${slug}/`, { next: { revalidate: 3600 } });
    if (!res.ok) return null;
    return await safeJson(res);
  } catch { return null; }
}

export async function getNews() {
  try {
    const res = await fetch(`${API_BASE}/api/news/`, { next: { revalidate: 900 } });
    if (!res.ok) return { results: [] };
    return await safeJson(res);
  } catch { return { results: [] }; }
}