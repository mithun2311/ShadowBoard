import { useParams } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import {
  BrainCircuit,
  ShieldAlert,
  BadgeCheck,
  LoaderCircle,
} from "lucide-react";

import { api } from "../lib/api";
import type { Decision } from "../types";

export default function DecisionPage() {
  const { id } = useParams();

  const { data: decision } = useQuery<Decision>({
    queryKey: ["decision", id],
    queryFn: async () =>
      (await api.get(`/api/v1/decisions/${id}`)).data,

    refetchInterval: (query) =>
      query.state.data?.status === "completed" ||
      query.state.data?.status === "failed"
        ? false
        : 2000,
  });

  if (!decision) {
    return (
      <div className="min-h-screen bg-slate-100 flex items-center justify-center">
        <LoaderCircle className="animate-spin text-slate-600" size={40} />
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-100">

      <header className="bg-white border-b border-slate-200">
        <div className="max-w-6xl mx-auto px-6 py-5">

          <p className="text-sm text-slate-500">
            Decision Analysis
          </p>

          <h1 className="text-3xl font-bold text-slate-900 mt-1">
            {decision.question}
          </h1>

          <div className="mt-3 inline-flex px-3 py-1 rounded-full bg-slate-200 text-sm">
            Status: {decision.status}
          </div>

        </div>
      </header>

      <main className="max-w-6xl mx-auto p-6 space-y-6">

        {decision.status !== "completed" &&
          decision.status !== "failed" && (
            <div className="bg-amber-50 border border-amber-200 rounded-xl p-6 flex items-center gap-4">

              <LoaderCircle
                className="animate-spin text-amber-600"
                size={22}
              />

              <div>

                <h3 className="font-semibold text-amber-900">
                  AI Board Deliberation
                </h3>

                <p className="text-amber-700 text-sm">
                  Agents are reviewing uploaded documents and
                  evaluating strategic options.
                </p>

              </div>

            </div>
          )}

        {decision.status === "completed" && (
          <>

            <section className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6">

              <div className="flex items-center gap-3 mb-4">
                <BadgeCheck className="text-green-600" />
                <h2 className="text-xl font-semibold">
                  Final Recommendation
                </h2>
              </div>

              <p className="text-slate-700 leading-7">
                {decision.final_recommendation}
              </p>

              <div className="mt-6">

                <span className="inline-flex rounded-full bg-green-100 text-green-700 px-4 py-2 text-sm font-medium">
                  Confidence: {decision.confidence_score}%
                </span>

              </div>

            </section>

            <section className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6">

              <div className="flex items-center gap-3 mb-4">
                <ShieldAlert className="text-red-500" />
                <h2 className="text-xl font-semibold">
                  Risk Assessment
                </h2>
              </div>

              <ul className="space-y-3">

                {decision.risk_summary?.key_risks.map(
                  (risk, index) => (
                    <li
                      key={index}
                      className="border rounded-lg p-3 bg-slate-50"
                    >
                      {risk}
                    </li>
                  )
                )}

              </ul>

            </section>

            <section className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6">

              <div className="flex items-center gap-3 mb-6">
                <BrainCircuit className="text-indigo-600" />
                <h2 className="text-xl font-semibold">
                  Agent Discussion
                </h2>
              </div>

              <div className="space-y-5">

                {decision.agent_transcript?.round2.map(
                  (agent, index) => (
                    <div
                      key={index}
                      className="border rounded-xl p-5 bg-slate-50"
                    >
                      <div className="flex justify-between items-center">

                        <h3 className="font-semibold text-slate-900">
                          {agent.agent}
                        </h3>

                        <span className="text-sm bg-indigo-100 text-indigo-700 px-3 py-1 rounded-full">
                          {agent.confidence}% Confidence
                        </span>

                      </div>

                      <p className="mt-4 text-slate-700 leading-7">
                        {agent.summary}
                      </p>

                      <div className="mt-4 border-l-4 border-indigo-500 pl-4 italic text-slate-600">
                        {agent.recommendation}
                      </div>

                    </div>
                  )
                )}

              </div>

            </section>

          </>
        )}

      </main>

    </div>
  );
}