---
name: poland-vehicles-road-xopoko
title: Poland Vehicles and Road Administration
description: 'Vehicles and road administration: route registration, ownership, inspections, compulsory insurance, tolls, parking, fines, and road incidents. Driving-licence matters stay separate.'
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-vehicles-road
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: administrative
language: en
---

# Poland Vehicles and Road Administration

Use for vehicle registration or deregistration, ownership changes, registration
documents and plates, technical inspections, compulsory third-party insurance,
tolls, parking administration, road charges, fines, and administrative steps
after a collision. Use `poland-transport-driving` for driving-licence exchange,
recognition, and rail/passenger rights.

Establish the vehicle and procedure category, acquisition/import context,
locality, date, requested effect, and whether safety, insurance, police, tax,
customs, or court issues are involved. Keep VIN, registration, policy, address,
and payment identifiers out of bundled tools.

Identify the competent starosta/city, registry, insurer, toll operator, police,
tax authority, or court and show official source IDs, current channels, locally
varying appointments, physical-document or plate handling, and live fee or
deadline checks. Read `../../references/life-events-and-services.md`,
`../../references/daily-life-map.md`, and
`../../references/locality-and-appointments.md`.

Use `vehicle-roadworthiness-and-oc` for technical inspection and public OC
checks; a registry result is not a roadworthiness, safety, ownership, policy or
legal-compliance conclusion, and the agent does not select an insurer or buy a
policy. Use `road-tolls-and-local-parking` with an exact route, vehicle/trailer
combination and mandatory `target_date`: the e-TOLL rule identified in the
packaged transition source changes on 2026-09-21, e-TOLL is not every concession
motorway toll, and local parking requires the current BIP resolution, road
manager and signage. Use `imported-vehicle-customs-and-excise` to separate
non-EU import, intra-EU acquisition, registration and PUESC excise; never infer
classification, valuation, exemption, tax base or liability.

For an authorized portal workflow, apply
`../../references/automation-playbook.md`. The user authenticates and controls
signatures, insurance choices, admissions, and final payment authorization. The
agent may navigate and prepare reviewable fields; submit, send, book, cancel,
pay, upload, download, or alter a record needs fresh action-time confirmation.
Never infer liability, coverage, title, customs status, or validity from a
single record.

Route a collision with possible injury to `poland-emergency-rights`, foreign
document issues to `poland-foreign-documents`, tax to `poland-tax`, and a fine
or dispute requiring legal judgment to `poland-justice-legal-aid`.
