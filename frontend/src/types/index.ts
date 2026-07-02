export interface AgentOutput {
  agent: string;
  summary: string;
  recommendation: string;
  confidence: number;
  risks:
    | string[]
    | {
        description: string;
        likelihood: string;
        impact: string;
      }[];
  citations: string[];
  revised?: boolean;
}

export interface Decision {
  id: string;
  project_id: string;
  question: string;
  status: "pending" | "running" | "completed" | "failed";
  final_recommendation: string | null;
  confidence_score: number | null;
  agent_transcript: {
    round1: AgentOutput[];
    round2: AgentOutput[];
    synthesis: any;
  } | null;
  risk_summary: {
    key_risks: string[];
    dissenting_views: string[];
  } | null;
  created_at: string;
  completed_at: string | null;
}

export interface DocumentItem {
  id: string;
  filename: string;
  doc_type: string;
  status: string;
  page_count: number | null;
  chunk_count: number;
}